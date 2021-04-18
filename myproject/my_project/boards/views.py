from django.shortcuts import get_object_or_404, render, resolve_url
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post,Comment,Board,Favorite
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import F
from django.http import HttpResponse, request


# Create your views here.

# class PostListView(ListView):
#     model = Post

class PostListView(ListView):
    model = Post
    template_name = 'boards/post_list.html'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # current_board = super(PostListView,self).get_context_data(**kwargs)
        if 'board_pk' in self.kwargs:
            pk = self.kwargs['board_pk']
            # current_board['current_board'] = Board.objects.get(pk=pk)
            context['current_board'] = Board.objects.get(pk=pk)
            # return current_board
        context['board_list'] = Board.objects.all().order_by('-visit_count')[:5]
        context['post_key_from_view'] = self.request.GET.get('key','').strip()
        return context

    def get_queryset(self):
        in_board = super().get_queryset()
        searched_list = super().get_queryset()
        # search_by = self.request.GET.get()
        key = self.request.GET.get('key','').strip()

        if 'board_pk' in self.kwargs:
            pk = self.kwargs['board_pk']
            Board.objects.filter(pk=pk).update(visit_count=F('visit_count')+1)
            in_board = Post.objects.filter(belong=pk)
            if key:
                searched_list = in_board.filter(title__contains = key)
                return searched_list
            print(pk)
            return in_board
                
        else :
            if key:
                searched_list = Post.objects.filter(title__contains = key)
                print(key)
                pk = 0
            return searched_list
            

            
        # print(key)
        # print(searched_list)
        

# class EachListView(ListView):
#     model = Post
#     template_name = 'boards/each_list'
#     def get_context_data(self, **kwargs):
#         context = super(EachListView,self).get_context_data(**kwargs)
#         context['board_list'] = Board.objects.all()
#         return context

#     def get_queryset(self):
#         post_list= super().get_queryset()
#         pk = self.kwargs['pk']
#         #post_list = Post.objects.select_related('belong').get(id=num)
#         post_list = Post.objects.filter(belong=pk)
#         print(pk)
#         return post_list


class BoardListView(ListView):
        model = Board
        template_name = 'boards/board_list.html'
        context_object_name = 'board_list'
        paginate_by =10


        def get_queryset(self):
            searched_board = super().get_queryset()
            search_by = self.request.GET.get('select')
            board_key = self.request.GET.get('board_key','').strip()
            if board_key:
                if search_by == 'board_name':
                    searched_board = Board.objects.filter(board_name__contains=board_key)
                else :
                    searched_board = Board.objects.filter(about__contains=board_key)
                print(searched_board)
                print(search_by)
            return searched_board

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["board_key_from_view"] = self.request.GET.get('board_key','').strip()
            
            return context
        



class PostLCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board_list"] = Board.objects.all()
        return context
    

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        # if 'board_pk' in self.kwargs:
        #     post.belong = Board.objects.filter(pk=self.kwargs['board_pk'])  
        print(post.belong)
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        Post.objects.filter(pk=pk).update(view_count=F('view_count')+1)
        return super().get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form']=CommentForm
        return context
    

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html'
    
    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('boards:post_list')

    def test_func(self):
        return self.request.user == self.get_object().author

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = get_object_or_404(Post, pk = self.kwargs['post_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('boards:post_detail',self.kwargs['post_pk'])


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    #success_url = reverse_lazy('boards:post_list')

    def test_func(self):
        return self.request.user == self.get_object().author
    def get_success_url(self):
        return resolve_url('boards:post_detail',self.kwargs['post_pk'])
